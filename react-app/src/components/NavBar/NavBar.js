
import React, { useState, useEffect } from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';
import { useDebounce } from '../../hooks/useDebounce'
import './navbar.css'
const NavBar = () => {
  const [profileDropDown, setProfileDropDown] = useState(false)
  const [showSearch, setShowSearch] = useState(false);
  const user = useSelector(state => state.session.user);
  const [search, setSearch] = useState('')
  const [users, setUsers] = useState([])
  const [filteredSearch, setFilteredSearch] = useState([])
  const [aboutDropDown, setShowAboutDropdown] = useState(false)
  const debouncedSearch = useDebounce(search, 315);
  const history = useHistory()


  const openSearchDropdown = () => {
    if (showSearch) return;
    setShowSearch(true)
  }


  useEffect(() => {
    if (!user) return;
    searchUsers(search, user.id)
  }, [debouncedSearch])

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('/api/users/');
      const responseData = await response.json();
      setUsers(responseData.users);
    }
    fetchData();
  }, []);

  const searchUsers = (search, id) => {
    let lowerSearch = search.toLowerCase()
    const filteredUsers = users.filter(user => {
      return user.username.toLowerCase().startsWith(lowerSearch) && user.id !== id
    })
    if (search !== '') setFilteredSearch(filteredUsers)
    else setFilteredSearch([])
  }


  let _handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      if (filteredSearch.length !== 0) {
        history.push(`/users/${filteredSearch[0].id}`)
      }
    }
  }
  const handleSearchChange = (e) => {
    setSearch(e.target.value)
    openSearchDropdown()
  }
  useEffect(() => {
    if (!showSearch) return;

    const closeActivity = () => {
      setShowSearch(false);
    };
    document.addEventListener('click', closeActivity);

    return () => document.removeEventListener("click", closeActivity);
  }, [showSearch]);

  useEffect(() => {
    if (!profileDropDown) return;

    const closeMenu = () => {
      setProfileDropDown(false);
    };
    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [profileDropDown]);

  useEffect(() => {
    if (!aboutDropDown) return;

    const closeMenu = () => {
      setShowAboutDropdown(false);
    };
    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [aboutDropDown]);


  return (
    <nav className='nav-bar'>
      <div className='inner-nav'>
        <NavLink to='/' exact={true} activeClassName='active'>
          <h2>SportsTube</h2>
        </NavLink>
        <input
          className='search-bar'
          placeholder='Search'
          value={search}
          onKeyDown={_handleKeyDown}
          onChange={handleSearchChange}
        >
        </input>
        {filteredSearch && showSearch && (<ul className='search-dropdown'>
          {filteredSearch && showSearch && filteredSearch.map(user =>
            <li key={`${user.id}`}><NavLink to={`/users/${user?.id}`}><img className='home-img' src={`${user.profileImgUrl}`} alt={user.username}></img></NavLink><NavLink to={`/users/${user?.id}`}>{`${user.username}`}</NavLink></li>
          )}
        </ul>)}

        <NavLink to='/' exact={true} activeClassName='active'>
          <i className="fas fa-home"></i>
        </NavLink>
        <button onClick={() => setShowAboutDropdown(true)}> About Me</button>
        <button className='home-img' onClick={() => setProfileDropDown(true)} style={{ backgroundImage: `url(${user?.profileImgUrl})` }}></button>

        {profileDropDown && (
          <ul className='profile-dropdown'>
            <li>
              <NavLink to={`/users/${user.id}`}>My Channel</NavLink>
            </li>
            <li>
              <LogoutButton />
            </li>
          </ul>
        )}

        {aboutDropDown && (
          <ul className='about-me-dropdown'>


            <div className="about-me">

              <li>Curtis Bridge</li>
              <li><a href='https://github.com/C-Bridge17' target='blank'>
                <i className="fab fa-github-square icon"></i>
              </a>
                <a href='https://www.linkedin.com/in/curtis-bridge-b126b121a/' target='blank'>
                  <i className="fab fa-linkedin icon"></i>
                </a>
              </li>

              <li className='copy'>&copy; Copyright 2021, curtis</li>
            </div>
          </ul>
        )}
      </div>
    </nav >
  );
}

export default NavBar;
