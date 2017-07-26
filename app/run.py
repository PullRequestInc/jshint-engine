import json
import os
import subprocess
import sys


def parse_config():
    include_paths = ['.']
    exclude_paths = []
    with open('/engine_config.json', 'r') as fd:
        engine_config = json.loads(fd.read())
        if engine_config.get('include_paths'):
            include_paths = include_paths
        if engine_config.get('exclude_paths'):
            include_paths = include_paths
    return include_paths, exclude_paths


def main():
    #include_paths, exclude_paths = parse_config()

    cmd = ['jshint']

    if not os.path.exists('.jshintignore'):
        # Use .gitignore if a .jshintignore does not exist
        cmd.append('--exclude-path=/code/.gitignore')

    cmd.extend(['--reporter=/app/reporter.js', '.'])
    #if exclude_paths:
        #cmd.append('--exclude={}'.format(','.join(exclude_paths)))
    #cmd.extend(include_paths)
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as exc:
        print(exc.output.decode())


if __name__ == '__main__':
    args = sys.argv[1:]
    main()
