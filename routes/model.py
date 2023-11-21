from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Date, Text, BigInteger, func
from sqlalchemy.orm import relationship
from settings.database import Base
from datetime import date, datetime
import random



class Order(Base):

    __tablename__ = "zfw_orders"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    ee_order_id = Column(String(255), nullable=True)
    ee_invoice_number = Column(String(255), nullable=True)
    reference_code = Column(String(100), nullable=True)
    sub_warehouse_id = Column(BigInteger, nullable=True)
    market_place_id = Column(Integer, nullable=True)
    market_place = Column(String(255), nullable=True)
    order_type = Column(String(255), nullable=True)
    replacement_order = Column(Integer, nullable=True)
    order_date = Column(DateTime(timezone=True), nullable=True)
    delivered_date = Column(DateTime(timezone=True), nullable=True)
    invoice_date = Column(DateTime(timezone=True), nullable=True)
    qc_passed = Column(Integer, nullable=True)
    manifest_no = Column(String(255), nullable=True)
    batch_id = Column(Integer, nullable=True)
    batch_created_at = Column(DateTime(timezone=True), nullable=True)
    total_amount = Column(Integer, nullable=True)
    total_tax = Column(Integer, nullable=True)
    total_discount = Column(Integer, nullable=True)
    courier = Column(String(255), nullable=True)
    shipping_status = Column(String(255), nullable=True)
    shipping_status_id = Column(Integer, nullable=True)
    tax_type = Column(String(255), nullable=True)
    total_shipping_charge = Column(Integer, nullable=True)
    payment_mode = Column(String(255), nullable=True)
    payment_mode_id = Column(Integer, nullable=True)
    awb_no = Column(String(255), nullable=True)
    billing_name = Column(String(255), nullable=True)
    billing_mobile = Column(String(50), nullable=True)
    billing_address_1 = Column(String(255), nullable=True)
    billing_address_2 = Column(String(255), nullable=True)
    billing_email = Column(String(50), nullable=True)
    billing_lat = Column(String(25), nullable=True)
    billing_long = Column(String(25), nullable=True)
    customer_name = Column(String(255), nullable=True)
    contact_num = Column(String(50), nullable=True)
    address_line_1 = Column(String(255), nullable=True)
    address_line_2 = Column(String(255), nullable=True)
    email = Column(String(50), nullable=True)
    latitude = Column(String(25), nullable=True)
    longitude = Column(String(25), nullable=True)
    pin_code = Column(Integer, nullable=True)
    package_weight = Column(Integer, nullable=True)
    brand_id = Column(BigInteger, nullable=True)
    easyecom_invoice = Column(String(255), nullable=True)
    label = Column(String(255), nullable=True)
    transaction_created = Column(Boolean, default=False, nullable=True)
    order_status = Column(String(255), nullable=True)
    order_status_id = Column(Integer, nullable=True)
    added_on = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_on = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
    added_by_id = Column(BigInteger, nullable=True)
    updated_by_id = Column(BigInteger, nullable=True)


class States(Base):
    __tablename__ = "zfw_states"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=True)
