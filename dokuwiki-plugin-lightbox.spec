%define		plugin		lightbox
Summary:	DokuWiki Lightbox plugin
Summary(pl.UTF-8):	Wtyczka lightbox dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20120103
Release:	0.10
License:	GPL v2
Group:		Applications/WWW
#Source0:	https://github.com/downloads/glensc/dokuwiki-plugin-lightboxv2/lightbox-%{version}.tar.bz2
Source0:	https://github.com/glensc/dokuwiki-plugin-lightboxv2/tarball/master/%{plugin}-%{version}.tgz
# Source0-md5:	156c43be191bebf757874d1a7c8ca67b
Source1:	https://github.com/krewenki/jquery-lightbox/tarball/master/jquery-lightbox.tgz
# Source1-md5:	14b30ba99c15cf2bb52af3ae21398969
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
%setup -qc -a1
mv *-%{plugin}v2-*/* .
mv *-jquery-lightbox-*/* jquery-lightbox

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ $(echo "$version" | tr -d -) != %{version} ]; then
	: %%{version} mismatch, should be: $(echo "$version" | tr -d -)
	exit 1
fi

%build
sh -x build.sh
tar xjf lightbox-*.tar.bz2

%install
rm -rf $RPM_BUILD_ROOT
cd %{plugin}
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/AUTHORS

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
%{plugindir}/*.txt
%{plugindir}/images
