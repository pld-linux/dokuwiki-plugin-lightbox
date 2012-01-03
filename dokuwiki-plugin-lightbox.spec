%define		plugin		lightbox
Summary:	DokuWiki Lightbox plugin
Summary(pl.UTF-8):	Wtyczka lightbox dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20120103
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/downloads/glensc/dokuwiki-plugin-lightboxv2/lightbox-%{version}.tar.bz2
# Source0-md5:	5e2d78e8eaeb03288ff838be23214c7d
URL:		http://www.dokuwiki.org/plugin:lightboxv2
Requires:	dokuwiki >= 20111110
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Plugin to integrate Lightbox JavaScript animation in DokuWiki.

%prep
%setup -qc
mv %{plugin}/* .

version=$(cat VERSION)
if [ $(echo "$version" | tr -d -) != %{version} ]; then
	: %%{version} mismatch, should be: $(echo "$version" | tr -d -)
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{AUTHORS,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.js
%{plugindir}/images
