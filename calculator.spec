Name:           CalcBuffaloBinary
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
Source0:        CalcBuffaloBinary-1.0.tar.gz

Requires:       postgresql

%description
This is a description

%prep
mkdir -p %{buildroot}/%{_bindir}

cp /home/runner/rpmbuild/SOURCES/%{name}  %{buildroot}/%{_bindir}/%{name}

%setup

%build
make 

%install
make install

%files
%{_bindir}/%{name}
