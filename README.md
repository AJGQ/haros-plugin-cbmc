# HAROS CBMC Plugin

This is a [HAROS](https://github.com/git-afsantos/haros/) plugin that analyses ROS nodes annotated with [HPL](https://github.com/git-afsantos/hpl-specs/) properties, using [CBMC](https://www.cprover.org/cbmc/).

## Installing

To install this package, make sure that you have Python 2.7 or Python 3.6+.
It is assumed that you **have CBMC installed or otherwise available** in your system, before using this tool.

You can either install a pre-packaged release,

```bash
pip install haros-plugin-cbmc
```

Or you can install from source.

```bash
git clone [REPO URL]
cd haros-plugin-cbmc
pip install -e .
```

## Usage

Start by defining annotated nodes in HAROS project files, as you normally would.

```yaml
%YAML 1.1
---
project: Fictibot
packages:
  - fictibot_drivers
  - fictibot_controller
  - fictibot_multiplex
  - fictibot_msgs
nodes:
  fictibot_controller/fictibot_controller:
    hpl:
      properties:
        - "globally: no /controller_cmd {data > PI}"
        - "globally: no /controller_cmd {data < -PI}"
```

## Bugs, Questions and Support

Please use the issue tracker.

## Citing

See [CITING](./CITING.md).

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md).

## Acknowledgment

This work is financed by ...
