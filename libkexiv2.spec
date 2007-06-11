Summary:	libkexiv2 - picture metadata manipulation library
Summary(pl.UTF-8):	libkexiv2 - biblioteka do obróbki metadanych obrazków
Name:		libkexiv2
Version:	0.1.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	8d273bf0ce692a814a0945c0664e116a
URL:		http://www.kipi-plugins.org/drupal/
BuildRequires:	exiv2-devel
BuildRequires:	kdelibs-devel >= 9:3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata. This library is used by kipi-plugins, digiKam and others
kipi host programs.

%description -l pl.UTF-8
libkexiv2 to obudowanie biblioteki Exiv2 do obróbki metadanych
obrazków. Ta biblioteka jest wykorzystywana przez pakiety
kipi-plugins, digiKam i inne programy oparte na kiki.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	exiv2-devel
Requires:	kdelibs-devel >= 9:3.4.0

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE.rev PACKAGING
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
