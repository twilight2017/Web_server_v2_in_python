from fabric.api import local


#def test():
    # 测试是否能正常运行
    #local('python manage.py test app')


def commit():
    local('git add -p && git commit -m "for test"')


def push():
    local('git push origin main')


def prepare_deploy():
    #test()
    commit()
    push()