def query_3():
    db_path = input()
    global_init(db_path)
    db_sess = create_session()

    query = db_sess.query(User).filter(User.age < 18)

    for i in query:
        print(i)


if __name__ == '__main__':
    query_3()
