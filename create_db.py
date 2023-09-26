from app import app, db, User

# Asegúrate de que la aplicación esté en modo de desarrollo
app.config['ENV'] = 'development'

# Crea la base de datos
with app.app_context():
    db.create_all()

    # Crea dos usuarios
    user1 = User(username='admin', password='adminpassword', email='admin@admin.com')
    user2 = User(username='user', password='userpassword', email='user@user.com')

    # Agrega los usuarios a la sesión y guarda en la base de datos
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

print("Base de datos creada y usuarios agregados exitosamente.")

