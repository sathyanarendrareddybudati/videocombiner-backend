from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StatesOUT(BaseModel):
    id: int
    name : str

    class Config:
        from_attributes=True

class OrderOUT(BaseModel):
    id: Optional[int]
    ee_order_id: Optional[str]
    ee_invoice_number: Optional[str]
    reference_code: Optional[str]
    sub_warehouse_id: Optional[int]
    market_place_id: Optional[int]
    market_place: Optional[str]
    order_type: Optional[str]
    replacement_order: Optional[int]
    order_date: Optional[datetime]
    delivered_date: Optional[datetime]
    invoice_date: Optional[datetime]
    qc_passed: Optional[int]
    manifest_no: Optional[str]
    batch_id: Optional[int]
    batch_created_at: Optional[datetime]
    total_amount: Optional[int]
    total_tax: Optional[int]
    total_discount: Optional[int]
    courier: Optional[str]
    shipping_status: Optional[str]
    shipping_status_id: Optional[int]
    tax_type: Optional[str]
    total_shipping_charge: Optional[int]
    payment_mode: Optional[str]
    payment_mode_id: Optional[int]
    awb_no: Optional[str]
    billing_name: Optional[str]
    billing_mobile: Optional[str]
    billing_address_1: Optional[str]
    billing_address_2: Optional[str]
    billing_email: Optional[str]
    billing_lat: Optional[str]
    billing_long: Optional[str]
    customer_name: Optional[str]
    contact_num: Optional[str]
    address_line_1: Optional[str]
    address_line_2: Optional[str]
    email: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    pin_code: Optional[int]
    package_weight: Optional[int]
    brand_id: Optional[int]
    easyecom_invoice: Optional[str]
    label: Optional[str]
    transaction_created: Optional[bool]
    order_status: Optional[str]
    order_status_id: Optional[int]
    added_on: Optional[datetime]
    updated_on: Optional[datetime]
    added_by_id: Optional[int]
    updated_by_id: Optional[int]

    class Config:
        from_attributes=True


class DeleteOrder(BaseModel):
    order_id : int

    class Config:
        from_attributes=True