from basic import db, Puppy, app

# CREATES ALL THE TABLES Model --> Db Table
with app.app_context():
    db.create_all()

    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)

    print(sam.name)
    print(frank.name)

    # Add row for all
    db.session.add_all([sam, frank])
    db.session.commit()

    print(sam.name)
    print(frank.name)

# Add row for one by one
# db.session.add(sam)
# db.session.add(frank)
