"""
Processor module for core backtest engine execution.

This module validates incoming backtest job requests and simulates execution.
In a real implementation, this would run a backtest loop over historical data.
"""

from typing import Any

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """
    Validate the incoming backtest job message.

    Args:
        message (dict[str, Any]): Raw message payload.

    Returns:
        ValidatedMessage: A validated message object.

    Raises:
        ValueError: If validation fails.
    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Invalid message schema: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def run_backtest_job(message: ValidatedMessage) -> dict[str, Any]:
    """
    Simulate execution of a backtest job based on input configuration.

    Args:
        message (ValidatedMessage): Validated job parameters.

    Returns:
        dict[str, Any]: Backtest result including simulated metrics.
    """
    job_id = message.get("job_id", "unknown")
    strategy = message.get("strategy", "unspecified")
    symbol = message.get("symbol", "UNKNOWN")
    logger.info("🧪 Running backtest job %s for %s using strategy %s", job_id, symbol, strategy)

    # Placeholder simulated result
    result = {
        "job_id": job_id,
        "symbol": symbol,
        "strategy": strategy,
        "status": "completed",
        "metrics": {
            "return_pct": 12.4,
            "sharpe_ratio": 1.7,
            "max_drawdown": -4.8,
        },
    }

    logger.debug("✅ Backtest job %s result: %s", job_id, result)
    return {**message, **result}
