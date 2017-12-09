import click
from pexpect import pxssh

#  from config import amo05, amo07, amo09, amo10
from config import amo09

s = pxssh.pxssh()


def date():
    s.sendline('date')       # run a command
    s.prompt()                # match the prompt
    print(s.before.decode('unicode_escape'))


@click.command()
@click.argument('server', type=str)
def pex(server):
    try:
        if server == 'amo9':
            s.login(amo09.ip, amo09.user, amo09.pwd)
            date()
            s.sendline('sudo su -')
            s.expect('assword.*: ')
            s.sendline(amo09.pwd)
            s.interact()
        else:
            return click.echo('Server Specified Not Found')

    except pxssh.ExceptionPxssh as e:
        print(e)
