from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Invoice(Base):
    """Model that tracks invoices created"""
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True) 
    client_name: Column(String, nullable=False)
    amount: Column(Float, nullable=False)

    items = relationship("InvoiceItem", back_populates="invoice")


class InvoiceItem(Base):
    """Model for items to be invoiced"""
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    product_name = Column(String, nullable=False )
    description: Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)


    invoice = relationship("Invoice", back_populates="items")
    product = relationship("Products", back_populates="products")


class Products(Base):
    """Model for products to be invoiced on"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    source = Column(String)

    products = relationship("InvoiceItem", back_populates="product")

