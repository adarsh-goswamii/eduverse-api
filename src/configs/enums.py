import enum

class VideoTranscodingStatus(enum.Enum):
  PENDING = "pending"
  PROCESSING = "processing"
  FAILED = "failed"
  COMPLETED = "completed"