import re
class DateTime:
  
  @classmethod
  def iso8601_to_seconds(self, duration: str) -> int:
    # Regex pattern to match the duration components
    pattern = r'P(?:\d+Y)?(?:\d+M)?(?:\d+D)?T?(?:\d+H)?(?:\d+M)?(?:\d+S)?'

    # Match the duration string to the regex pattern
    match = re.match(pattern, duration)

    if not match:
        raise ValueError("Invalid ISO 8601 duration format")

    total_seconds = 0

    # Extract hours, minutes, and seconds (if present)
    hours_match = re.search(r'(\d+)H', duration)
    minutes_match = re.search(r'(\d+)M', duration)
    seconds_match = re.search(r'(\d+)S', duration)

    # Add to total_seconds for each component found
    if hours_match:
        total_seconds += int(hours_match.group(1)) * 3600  # hours to seconds
    if minutes_match:
        total_seconds += int(minutes_match.group(1)) * 60  # minutes to seconds
    if seconds_match:
        total_seconds += int(seconds_match.group(1))  # seconds

    return total_seconds
  
datetime = DateTime