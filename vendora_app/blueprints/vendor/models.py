
from vendora_app.app import db
from flask_login import UserMixin
from datetime import datetime


class Vendor(db.Model):
    __tablename__ = 'vendors'
    
    # Core Identity and Key
    uid = db.Column(db.Integer, primary_key=True)  # Vendor ID
    business_name = db.Column(db.String(255), nullable=False, unique=True)
    contact_person = db.Column(db.String(100), nullable=False)
    
    # Contact Details
    primary_phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    website_url = db.Column(db.String(2048), nullable=True)

    # Description and Media
    short_description = db.Column(db.String(500), nullable=False)
    long_description = db.Column(db.Text, nullable=True)
    logo_url = db.Column(db.String(2048), nullable=True)
    
    # Financial & Legal
    gst_number = db.Column(db.String(50), nullable=True, unique=True)
    
    # Status and Moderation
    verification_status = db.Column(db.String(50), default='Pending', nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False) # 1 for live, 0 for paused

    # Metrics (Updated via joins/triggers)
    rating_average = db.Column(db.Numeric(3, 2), default=0.00, nullable=False)
    review_count = db.Column(db.Integer, default=0, nullable=False)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Vendor: {self.business_name}, ID: {self.uid}>'

    # --- Relationships ---
    # Example relationship for Addresses (assuming an 'Addresses' model exists)
    # addresses = db.relationship('Address', backref='vendor', lazy='dynamic')
    