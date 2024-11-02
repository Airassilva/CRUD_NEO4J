from main import create_user, get_users, update_user, delete_user, create_relationship, clear_database, db

def run_tests():
    print("Limpando o banco de dados...")
    clear_database()

    print("Criando usuários...")
    create_user("Alice", 18)
    create_user("Coelho Branco", 5)
    create_user ("Rainha de copas", 20)

    print("Listando usuários...")
    users = get_users()
    for user in users:
        print(user)

    print("Atualizando dados...")
    update_user("Alice", 16)

    print("Criando relacionamentos...")
    create_relationship("Alice", "Coelho Branco", "AMIGO")
    create_relationship("Alice", "Rainha de copas","INIMIGO")

    print("Listando usuários após criar relação...")
    users = get_users()
    for user in users:
        print(user)

    #print("Excluindo usuários...")
    #delete_user("Alice")
    #delete_user("Coelho Branco")

    #print("Limpando o banco de dados após os testes...")
    #clear_database()

if __name__ == "__main__":
    run_tests()
    db.close()



