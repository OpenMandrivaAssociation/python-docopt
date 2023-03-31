%global pypi_name docopt

Name:		python-docopt
Version:	0.6.2
Release:	12
Summary:	Pythonic argument parser, that will make you smile

License:	MIT
URL:		https://github.com/docopt/docopt
Source0:	%{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildArch:      noarch

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%license LICENSE-MIT
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info
%{python3_sitelib}/%{pypi_name}.py
