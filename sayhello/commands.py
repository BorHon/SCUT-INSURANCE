# -*- coding: utf-8 -*-
# A:the Children Health Insurance
# B:the family Health Insurance
# C:the specific disease Insurance,like the lung cancer Insurance
# D:the ordinary personal health Insurance

import click
from sayhello import app, db
from sayhello.models import Information
from sayhello.trainmodels import train_Information
from faker import Faker


def produce_train():
    fake = Faker()
    marriage_choice=["married","unmarried","divorced"]
    sex_choice=["Male","Female","UnKnown"]
    age=fake.random_int(min=18,max=92)
    if age<=18 or age>60:
        salary=0
        marriage="unmarried"
    else:
        salary=fake.random_int(min=0,max=100000)
        marriage=marriage_choice[fake.random_int(min=0,max=99) % 3]
    sex=sex_choice[fake.random_int(min=0,max=99) % 3]
    height = fake.random_int(min=140, max=190)
    weight = fake.random_int(min=30, max=200)
    BMI=weight/(height**2)
    insurance=""
    if age<12:
        insurance="A"
    if marriage=="married" and sex=="Male":
        insurance="B"
    if BMI<10 or  BMI>32:
        insurance="D"
    return age,salary,marriage,sex,height,weight,insurance


@app.cli.command()
def forges(count=100):
    """Generate training data."""
    from faker import Faker
    fake = Faker()
    click.echo('Working...')
    for i in range(count):
        age,salary,marriage,sex,height,weight,insurance=produce_train()
        train_information=train_Information(
            Age=age,
            Salary=salary,
            Marriage=marriage,
            Height=height,
            Weight=weight,
            Sex=sex,
            Insurance=insurance
        )
        # print(train_information.Insurance)
        db.session.add(train_information)
    db.session.commit()
    click.echo('Created %d fake messages.' % count)


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    # if drop:
    #     click.confirm('This operation will delete the database, do you want to continue?', abort=True)
    #     db.drop_all()
    #     click.echo('Drop tables.')
    db.drop_all()
    db.create_all()
    click.echo('Initialized database.')





