%global pypi_name docopt

Name:           python-docopt
Version:        0.6.2
Release:        10%{?dist}
Summary:        Pythonic argument parser, that will make you smile

License:        MIT
URL:            https://github.com/docopt/docopt
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools

BuildArch:      noarch

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%package -n python2-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{pypi_name}
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

Python 2 version.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE-MIT
%doc README.rst
%{python2_sitelib}/%{pypi_name}-*.egg-info/
%{python2_sitelib}/%{pypi_name}.py*

%files
%license LICENSE-MIT
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.*
