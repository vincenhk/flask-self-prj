from models import db, Puppy, Toy, Owner, app

with app.app_context():
    # # Create 2 Puppies
    # rufus = Puppy('rufus')
    # fido = Puppy('fido')
    #
    # # Add puppies to DB
    # db.session.add_all([rufus, fido])
    # db.session.commit()

    # Check all data!
    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name='rufus').first()

    # Create owner
    add = Owner('tina', rufus.id)

    # Give rufus some toys
    # toy1 = Toy('Chew Toy', rufus.id)
    # toy2 = Toy('Ball', rufus.id)

    # db.session.add_all([add, toy1, toy2])
    # db.session.add(add)
    # db.session.commit()

    # delete = db.session.get(Owner, 3)
    # db.session.delete(delete)
    # db.session.commit()

    # GRAB RUFUS AFTER THOSE ADDITION!
    # rufus = Puppy.query.filter_by(name='rufus').first()
    # print(rufus)
    # print(rufus.report_toys())
