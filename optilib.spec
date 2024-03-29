Summary:	Optilib - Linux Demo Scene library
Summary(pl.UTF-8):	Optilib - biblioteka dla linuksowej DemoSceny
Name:		optilib
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://optimum.sourceforge.net/optilib/%{name}-%{version}.tar.gz
# Source0-md5:	44d88e90e7196db4239dfb484d8c1f07
URL:		http://optimum.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Optilib is a library of functions dealing with X11 and images.

%description -l pl.UTF-8
Optilib jest biblioteką ułatwiającą pisanie demek scenowych pod
Linuksem dla X11.

%prep
%setup -q -n Optilib-%{version}

%build
%{__make} optilib

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/optilib
install -d $RPM_BUILD_ROOT%{_includedir}/optilib
install OptiLib/lib/optilib.a $RPM_BUILD_ROOT%{_libdir}/optilib/optilib.a
install OptiLib/include/* $RPM_BUILD_ROOT%{_includedir}/optilib/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/*
%{_includedir}/optilib/*
