from basic import db, Puppy, app

with app.app_context():
    ## CREATE ##
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

    ## READ ##
    all_puppy = Puppy.query.all()
    print(all_puppy)

    ## SELECT BY ID ##
    puppy_one = Puppy.query.get(1)
    print(puppy_one.name)

    # FILTERS
    # PRODUCE SOME SQL CODE!
    puppy_frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_frankie.all())

    ## UPDATE
    first_puppy = Puppy.query.get(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    ## DELETE
    second_puppy = Puppy.query.get(3)
    db.session.delete(second_puppy)
    db.session.commit()
