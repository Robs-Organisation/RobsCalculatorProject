Name:           calculator
Version:        1.0
Release:        1%{?dist}
Summary:        a calculator to learn something about gobuffalo

License:        All rights reserved
URL:            https://github.com/Robs-Organisation/RobsCalculatorProject
#Source0:        calculator-1.0.tar.gz

Requires:       postgresql

%description
This is a description

%setup -c

%prep
mkdir -p %{buildroot}/calc

cp CalcBuffaloBinary %{buildroot}/calc

%build

%install

%files
%defattr(0644, root,root)
/home/runner/work/RobsCalculatorProject/RobsCalculatorProject/CalcBuffaloBinary
