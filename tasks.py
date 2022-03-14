from invoke import task, Collection
import Web_server_v2_in_python.docs as docs


@task
def deploy(c):
    print("deploy successfully")


namespace = Collection(docs, deploy)