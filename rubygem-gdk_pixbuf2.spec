# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname gdk_pixbuf2

Summary:	Ruby binding of GdkPixbuf-2.x
Name:		rubygem-%{rbname}

Version:	2.2.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/gdk_pixbuf2-2.2.0.gem
BuildRequires:	rubygems 
BuildRequires:  rubygem(glib2)
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  rubygem-glib2-devel
Obsoletes:      ruby-gdkpixbuf2

%description
Ruby binding of GdkPixbuf-2.x.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%package    devel
Summary:    Development files for %{name}
Group:      Development/Ruby

%description    devel
Development files for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

%files devel
%{ruby_sitearchdir}/*.h
