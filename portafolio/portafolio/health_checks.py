from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def health_check(request):
    """
    Health check endpoint for Render.
    Returns a 200 OK response to indicate the service is running.
    """
    logger.info("Health check endpoint was called.")
    return HttpResponse("OK", status=200)

def ready_check(request):
    """
    Readiness check endpoint for Render.
    Can be expanded to check for database connectivity, etc.
    """
    logger.info("Readiness check endpoint was called.")
    return HttpResponse("OK", status=200)
