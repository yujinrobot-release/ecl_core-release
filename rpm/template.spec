Name:           ros-melodic-ecl-concepts
Version:        0.62.2
Release:        0%{?dist}
Summary:        ROS ecl_concepts package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_concepts
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-ecl-config
Requires:       ros-melodic-ecl-license
Requires:       ros-melodic-ecl-type-traits
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-ecl-config
BuildRequires:  ros-melodic-ecl-license
BuildRequires:  ros-melodic-ecl-type-traits

%description
Introduces a compile time concept checking mechanism that can be used most
commonly to check for required functionality when passing template arguments.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Sep 14 2018 Daniel Stonier <d.stonier@gmail.com> - 0.62.2-0
- Autogenerated by Bloom

* Sun May 13 2018 Daniel Stonier <d.stonier@gmail.com> - 0.62.1-0
- Autogenerated by Bloom

* Sat May 12 2018 Daniel Stonier <d.stonier@gmail.com> - 0.62.0-0
- Autogenerated by Bloom

