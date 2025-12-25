"""
Rate limiting configuration using slowapi
"""
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import Request
from fastapi.responses import JSONResponse

# Create limiter instance
limiter = Limiter(key_func=get_remote_address)


def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    """Custom handler for rate limit exceeded"""
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded. Please try again later.",
            "retry_after": str(exc.detail)
        }
    )


# Rate limit decorators for different endpoint types
# These are the limits per IP address

# Auth endpoints - stricter limits to prevent brute force
AUTH_LIMIT = "5/minute"

# Regular API endpoints
API_LIMIT = "60/minute"

# Execution endpoints - moderate limits
EXECUTE_LIMIT = "10/minute"

# Read-only endpoints - more relaxed
READ_LIMIT = "120/minute"
