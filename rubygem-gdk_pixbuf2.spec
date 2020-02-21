
%define	gem_name gdk_pixbuf2

Summary:	Ruby binding of GdkPixbuf-2.x
Name:		rubygem-%{gem_name}

Version:	3.4.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  rubygems-devel
BuildRequires:  rubygem-pkg-config
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  rubygem-native-package-installer
BuildRequires:	rubygem-rake

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


%prep
%setup -q -n  %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_extdir_mri}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

%files
%{gem_instdir}/lib/*.rb
%{gem_instdir}/sample/*.rb
%{gem_instdir}/sample/gnome-foot.png
%{gem_instdir}/sample/floppybuddy.gif
%{gem_instdir}/test/fixture/*
%{gem_instdir}/test/*.rb
%{gem_instdir}/lib/%{gem_name}/*
%{gem_instdir}/dependency-check/Rakefile
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_spec}
%{gem_cache}

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%{gem_instdir}/[A-Z]*
