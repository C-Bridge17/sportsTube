from app.models import db, User
from faker import Faker

faker = Faker()


# Adds a demo user, you can add other users here if you want
def seed_users():
    u1 = User(
        username='Demo', email='demo@aa.io', password='password')

    u2 = User(username='NBC Sports', email='u1@aa.io', password='password',
              profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLRzF9VGD3TH7g9ge0uGS2pOj1oGLB6qvyHEEI1eM4M=s88-c-k-c0x00ffffff-no-rj')
    u3 = User(username='AshStudio7', email='u3@aa.io',
              password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLSlaLGltLK8QJq342VSfn9J83dG56bWnySdoruMew=s68-c-k-c0x00ffffff-no-rj')
    u4 = User(username='Dude Perfect', email='u4@aa.io', password='password',
              profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLSw2IlUFHy6GUZw3OPu2FZ1i5H-YQTbPX92yRS3Ig=s68-c-k-c0x00ffffff-no-rj')
    u5 = User(username='Highlight Heaven', email='u5@aa.io', password='password',
              profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLRC89SwGr05ZzZHL3ucE2Qpr9RI2Qny0fkmIflgYg=s68-c-k-c0x00ffffff-no-rj')
    u6 = User(username='CBS Sports HQ', email='u6@aa.io',
              password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLRVzUmJX5whdKFHCtO59azqSPuu7ywo620CGMGlyg=s68-c-k-c0x00ffffff-no-rj')
    u7 = User(username='Savage Brick Sports', email='u7@aa.io',
              password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLQBHWydc7fBXk2CEQsyU6pRFxZe_0WpYEXxv9ErGw=s48-c-k-c0x00ffffff-no-rj')
    u8 = User(username='MAD LAB', email='u8@aa.io',
              password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLTSVEhmx718VrTIsakbTOFx9VZB_xFJqXOMNvDeNQ=s48-c-k-c0x00ffffff-no-rj')
    u9 = User(username='Comedy Central', email='u9@aa.io',
              password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLQZkoCl_qDlLP_Xfrd_A6JRv_0FtgdQKaQu4FfYBA=s48-c-k-c0x00ffffff-no-rj')
    u10 = User(username='ESPN', email='u10@aa.io', password='password',
               profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLT9EPEwNhuq_gfXvF5vzi5igtV1ijl8idOSy6s2cQI=s68-c-k-c0x00ffffff-no-rj')
    u11 = User(username='The Pat McAfee Show', email='u11@aa.io', password='password',
               profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLQnpO3sdJ0vL35RYzE-jlf1TbwcgN2dKzr0FIrV0Q=s48-c-k-c0x00ffffff-no-rj')
    u12 = User(username='PGA TOUR', email='u12@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/1u5DXc04sQw8jYFcQvfzyjI-HZkNjfUxuIc3MbnyAYlSgwSCwsuxwJ2eJTzEcZvWwbN-OkvNtw=s68-c-k-c0x00ffffff-no-rj')
    u13 = User(username='GQ Sports', email='u13@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLSUCu-F2mHJ4bTMVyZgCyT_UQ9WbJcEFvsH0Ws0=s68-c-k-c0x00ffffff-no-rj')
    u14 = User(username='Tampa Bay Buccaneers', email='u14@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLSvQFuxQDTPOsdVG4kDR9GhRCTgyBWHE40ZeJCeow=s68-c-k-c0x00ffffff-no-rj')
    u15 = User(username='Sports Illustrated', email='u15@aa.io', password='password',
               profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLQSyuMzImTFB9s726DYoy_xSbPuIpbHkLRaO1KuUGY=s48-c-k-c0x00ffffff-no-rj')
    u16 = User(username='Rick Shiels Golf', email='u16@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLT1fsdjZ8nRP4mCLnKr8PaXddbE0z9nOdI78vrgig=s48-c-k-c0x00ffffff-no-rj')
    u17 = User(username='Carmelo Anthony', email='u17@aa.io', password='password',
               profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLTfMUd1wYs5TwXOBvowh_8KzGvKSU_CCG5L0HyZ=s48-c-k-c0x00ffffff-no-rj')
    u18 = User(username='Cam Newton', email='u18@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLTfC_WtP1_NCFCHUHNmroe0omuH0H8mK41Bla4H=s88-c-k-c0x00ffffff-no-rj')
    u19 = User(username='Nonstop Sports', email='u19@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLQTOl_5XT2wKpSmmqFZrfTLM4uieQHLf6ar1CyshQ=s48-c-k-c0x00ffffff-no-rj')
    u20 = User(username='Spittin\' Chiclets', email='u20@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLRXLpsid6E36GAogs9eRBCQ7BMVI1qcjHXwSMxm=s48-c-k-c0x00ffffff-no-rj')
    u21 = User(username='Hammer Dahn', email='u21@aa.io',
               password='password', profileImgUrl='https://yt3.ggpht.com/ytc/AKedOLQcxheSSBQ78HJcTpfrJd9rG74eCK77JA9uNDlE=s88-c-k-c0x00ffffff-no-rj')

    list = [u1, u2, u3, u4, u5, u6, u7, u8, u9,
            u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u20, u21]
    for i in list:
        db.session.add(i)

    for i in range(50):
        user = User(username=faker.simple_profile()[
                    'username'], email=faker.simple_profile()['mail'], password=faker.password())
        u1.subscribers.append(user)
        u2.subscribers.append(user)
        u3.subscribers.append(user)
        u4.subscribers.append(user)
        u5.subscribers.append(user)
        u6.subscribers.append(user)
        u7.subscribers.append(user)
        u8.subscribers.append(user)
        u9.subscribers.append(user)
        u10.subscribers.append(user)
        u11.subscribers.append(user)
        u12.subscribers.append(user)
        u13.subscribers.append(user)
        u14.subscribers.append(user)
        u15.subscribers.append(user)
        u16.subscribers.append(user)
        u17.subscribers.append(user)
        u18.subscribers.append(user)
        u19.subscribers.append(user)
        u20.subscribers.append(user)
        u21.subscribers.append(user)
        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
