from fastapi import APIRouter , HTTPException
from app.schema.contacts import ContactCreate, ContactResponse, ContactUpdate, Category
from datetime import datetime
from typing import Optional

router = APIRouter(
    prefix= "/contacts",
    tags = ["contacts"]
)
contacts_db : list[dict] = []
next_id : int = 1
@router.post("/" , response_model=ContactResponse , status_code=201)
def creat_contact(contact : ContactCreate):
    global next_id
    new_contact = {
        "id" : next_id, **contact.model_dump(),  "created_at": datetime.now().isoformat()
                   }
    contacts_db.append(new_contact)
    next_id += 1
    return new_contact

@router.get("/", response_model=list[ContactResponse])
def list_contacts(category : Optional[Category] = None):
    if category:
        return[t for t in contacts_db if t.get["category"] == category.value]
    return contacts_db

@router.get("/{contact_id}", response_model=ContactResponse)
def list_contact(contact_id:int):
    for contact in contacts_db:
        if contact["id"] == contact_id:
            return contact
    raise HTTPException(status_code=404, detail="Contact not found") 

@router.patch("/{contact_id}", response_model= ContactResponse)
def update_contact(contact_id : int ,updates : ContactUpdate):
    for contact in contacts_db:
        if contact["id"] == contact_id:
            update_data = updates.model_dump(exclude_unset=True)
            contact.update(update_data)
            return contact
    raise HTTPException(status_code=404, detail="contact not found")



