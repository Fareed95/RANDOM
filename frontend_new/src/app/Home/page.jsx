"use client"
import React, { useEffect } from 'react';

function Page() {
  useEffect(() => {
    const fetchUser = async () => {
      try {
        const resp = await fetch("http://127.0.0.1:8000/api/user", {
          credentials: 'include'
        });
        const user = await resp.json();
        console.log(user);
      } catch (error) {
        console.error('Error fetching user:', error);
      }
    };

    fetchUser();
  }, []);

  return (
    <div>
      home
    </div>
  );
}

export default Page;
