from main import create_user, get_users, update_user, delete_user, create_relationship, clear_database, db

def run_tests():
    # Limpar o banco de dados antes de começar os testes
    print("Limpando o banco de dados...")
    clear_database()

    # Criar usuários
    print("Criando usuários...")
    create_user("Alice", 18)
    create_user("Coelho Branco", 5)
    create_user ("Rainha de copas", 20)

    # Listar usuários
    print("Listando usuários...")
    users = get_users()
    for user in users:
        print(user)

    # Atualizar usuário
    print("Atualizando dados...")
    update_user("Alice", 16)

    # Criar relação entre usuários
    print("Criando relacionamentos...")
    create_relationship("Alice", "Coelho Branco", "AMIGO")
    create_relationship("Alice", "Rainha de copas","INIMIGO")

    # Listar usuários novamente
    print("Listando usuários após criar relação...")
    users = get_users()
    for user in users:
        print(user)

    # Excluir usuários
    #print("Excluindo usuários...")
    #delete_user("Alice")
    #delete_user("Coelho Branco")

    # Limpar o banco de dados novamente
    #print("Limpando o banco de dados após os testes...")
    #clear_database()

if __name__ == "__main__":
    run_tests()
    # Fechar conexão com o banco de dados
    db.close()



