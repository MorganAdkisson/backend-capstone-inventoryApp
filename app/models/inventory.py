from app import db

class Inventory(db.Model):
    """
    Each Inventory for each tank will be it's own line of data in db table. 
    This is a 1 to 1 match with the spreadsheet used by PSRF to track inv. 
    """
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    inv_date=db.Column(db.DateTime)
    family=db.Column(db.String)
    facility=db.Column(db.String)
    tank=db.Column(db.String)
    task_id=db.Column(db.String)
    total_animals=db.Column(db.Integer)
    # shell_lengths will be stored as a string of float numbers separated by commas 
    shell_lengths=db.Column(db.String)

    def to_dict(self): 
        return {
        "id": self.id,
        "inv_date": self.inv_date.strftime("%m/%d/%Y"),
        "family": self.family,
        "facility": self.facility,
        "tank": self.tank,
        "task_id": self.task_id,
        "total_animals": self.total_animals,
        "shell_lengths": self.shell_lengths
        }
