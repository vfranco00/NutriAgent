from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Food(Base):
    __tablename__ = "foods"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    category: Mapped[str | None] = mapped_column(String(80), nullable=True)
    kcal_per_100g: Mapped[float | None] = mapped_column(Numeric(6,2))
    # Macro
    protein_g: Mapped[float | None] = mapped_column(Numeric(6,2))
    fat_g: Mapped[float | None] = mapped_column(Numeric(6,2))
    carbs_g: Mapped[float | None] = mapped_column(Numeric(6,2))