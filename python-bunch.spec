#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	module bunch
Summary:	Python dictionary with attribute-style access
Name:		python-bunch
Version:	1.0.1
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/b/bunch/bunch-%{version}.tar.gz
# Source0-md5:	0a829d64e95ed96defbcae2bf9061bb0
URL:		http://github.com/dsc/bunch
BuildRequires:	dos2unix
BuildRequires:	python-nose
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-bunch provides a Python class which can perform as a dict whose
keys are also accessible as attributes, similar to JavaScript objects.

The piece of python-bunch that sets it apart from similar modules
found inside other projects is the bunchify() function which
recursively converts from a dict to a Bunch.

%prep
%setup -q -n %{module}-%{version}
dos2unix LICENSE.txt README.rst

%build
%py_build

%if %{with tests}
PYTHONPATH=build/lib nosetests-%{py_ver} --with-doctest
PYTHONPATH=build/lib %{__python} build/lib/bunch/test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/bunch/test.*

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/bunch
%{py_sitescriptdir}/bunch-%{version}-py*.egg-info
