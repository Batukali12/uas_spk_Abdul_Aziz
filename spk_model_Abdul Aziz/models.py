from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class MotorSport(Base):
    __tablename__ = "motorsport"

    nama : Mapped[str] = mapped_column(primary_key=True)
    harga : Mapped[int]
    cc : Mapped[float]
    kapasitas_bensin : Mapped[float]
    daya_maksimum : Mapped[float]
    torsi_maksimum : Mapped[float]

    def __repr__(self) -> str :
        return f"nama={self.nama}, harga={self.harga}, cc={self.cc}, kapasitas_bensin={self.kapasitas_bensin}, daya_maksimum={self.daya_maksimum}, torsi_maksimum={self.torsi_maksimum}"
