Name: libatasmart
Version: 0.17
Release: 3%{?dist}
Summary: ATA S.M.A.R.T. Disk Health Monitoring Library
Group: System Environment/Libraries
Source0: http://0pointer.de/public/libatasmart-%{version}.tar.gz
License: LGPLv2+
Url: http://git.0pointer.de/?p=libatasmart.git;a=summary
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libudev-devel

# https://bugs.freedesktop.org/show_bug.cgi?id=25543
Patch0: libatasmart-uninitialized-var.patch

%description
A scmall and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package devel
Summary: Development Files for libatasmart Client Development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development Files for libatasmart Client Development

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%prep
%setup -q
%patch0 -p1 -b .uninitialized-var.patch

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm $RPM_BUILD_ROOT%{_docdir}/libatasmart/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LGPL
%{_libdir}/libatasmart.so.*
%{_sbindir}/skdump
%{_sbindir}/sktest

%files devel
%defattr(-,root,root)
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
%{_datadir}/vala/vapi/atasmart.vapi
%doc blob-examples/SAMSUNG* blob-examples/ST* blob-examples/Maxtor* blob-examples/WDC* blob-examples/FUJITSU* blob-examples/INTEL* blob-examples/TOSHIBA* blob-examples/MCC*

%changelog
* Tue Jan 12 2010 Matthias Clasen <mclasen@redhat.com> - 0.17-3
- Don't require vala (#547784)

* Wed Dec  9 2009 Matthias Clasen <mclasen@redhat.com> - 0.17-2
- Fix an unitialized variable that causes problems in udisks

* Tue Oct 27 2009 Lennart Poettering <lpoetter@redhat.com> 0.17-1
- New upstream release
- Fixes bug 491552

* Tue Sep 29 2009 Lennart Poettering <lpoetter@redhat.com> 0.16-1
- New upstream release
- Second try at fixing #515881

* Fri Sep 18 2009 Lennart Poettering <lpoetter@redhat.com> 0.15-1
- New upstream release
- Fixes #515881

* Thu Aug 6 2009 Lennart Poettering <lpoetter@redhat.com> 0.14-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Lennart Poettering <lpoetter@redhat.com> 0.13-1
- New upstream release

* Wed Apr 15 2009 Lennart Poettering <lpoetter@redhat.com> 0.12-1
- New upstream release

* Tue Apr 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.11-1
- New upstream release

* Mon Apr 13 2009 Lennart Poettering <lpoetter@redhat.com> 0.10-1
- New upstream release

* Sun Apr 12 2009 Lennart Poettering <lpoetter@redhat.com> 0.9-1
- New upstream release

* Fri Apr 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.8-1
- New upstream release

* Tue Apr 7 2009 Lennart Poettering <lpoetter@redhat.com> 0.7-1
- New upstream release

* Sat Apr 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.6-1
- New upstream release

* Fri Apr 3 2009 Lennart Poettering <lpoetter@redhat.com> 0.5-1
- New upstream release

* Thu Apr 2 2009 Lennart Poettering <lpoetter@redhat.com> 0.4-1
- New upstream release

* Tue Mar 24 2009 Lennart Poettering <lpoetter@redhat.com> 0.3-1
- New upstream release

* Thu Mar 19 2009 Lennart Poettering <lpoetter@redhat.com> 0.2-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 25 2008 Lennart Poettering <lpoetter@redhat.com> 0.1-1
- Initial version
