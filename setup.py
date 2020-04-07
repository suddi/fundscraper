# pylint: disable-msg=no-name-in-module,import-error
from distutils.cmd import Command
from os import getcwd
from subprocess import check_call
from setuptools import setup

class ComputePerformingFundsCommand(Command):
    description = 'calculate performing funds'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['python', '-m', 'scripts.compute_performing_funds']
        return check_call(command)

class ComputeReturnsCommand(Command):
    description = 'compute returns from db'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['python', '-m', 'scripts.compute_returns']
        return check_call(command)

class PylintCommand(Command):
    description = 'run pylint on Python source files'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['pylint', getcwd()]
        return check_call(command)

class ListCollectionsCommand(Command):
    description = 'list all the collections in db'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = ['python', '-m', 'scripts.list_collections']
        return check_call(command)

setup(cmdclass={
    'compute_performing_funds': ComputePerformingFundsCommand,
    'compute_returns': ComputeReturnsCommand,
    'lint': PylintCommand,
    'list_collections': ListCollectionsCommand
})
