Name:		optilib
Summary:	Optilib - Linux Demo Scene library
Summary(pl):	Optilib - biblioteka dla Linuksowej DemoSceny
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://optimum.sf.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://optimum.sf.net
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Optilib is a library of functions dealing with X11 and images.

%description -l pl
Optilib jest bibliotek± u³atwiaj±c± pisanie demek scenowych pod
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
%attr(644,root,root) %{_libdir}/*
%{_includedir}/optilib/*
