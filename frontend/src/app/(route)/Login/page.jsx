"use client";
import { useRouter } from "next/navigation";
import { useEffect, useState } from 'react';

function Page() {
    const router = useRouter();
    const [index, setIndex] = useState(null);
    const [formData, setFormData] = useState({
        username: "",
        password: ""
    });
    const [data, setData] = useState([]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const Submit = async (e) => {
        e.preventDefault();

        const getData = async () => {
            const query = await fetch('http://127.0.0.1:8000/users');
            const resp = await query.json();
            setData(resp);
            checkData(resp);  // Call checkData function with the fetched data
        };

        getData();
    };

    const checkData = (data) => {
        let found = false;
        data.forEach(i => {
            if (i.username === formData.username && i.password === formData.password) {
                setIndex(i.id);
                found = true;
            }
        });

        if (found) {
            console.log("equal");
        } else {
            alert("Username and password do not match");
        }
    };

    useEffect(() => {
        if (index !== null) {
            router.push(`Main/${index}`);
            // Immediately reset the index after triggering the navigation
            setIndex(null);
        }
    }, [index, router]);

    return (
        <div>
            <div className="flex items-center justify-center h-[7rem] ">
                <div className="text-6xl font-bold bg-gradient-to-r from-blue-500 via-purple-400 to-pink-700 bg-clip-text text-transparent transition-colors duration-1000 hover:bg-gradient-to-r hover:from-blue-800 hover:via-purple-600 hover:to-pink-400 ease-in">
                    LOGIN
                </div>
            </div>

            <section className="text-gray-600 body-font relative">
                <div className="container px-5 py-24 mx-auto">
                    <div className="flex flex-col text-center w-full mb-12">
                        <p className="lg:w-2/3 mx-auto leading-relaxed text-base">Fill out the form below to see the details on another page.</p>
                    </div>
                    <div className="lg:w-1/2 md:w-2/3 mx-auto">
                        <form onSubmit={Submit}>
                            <div className="flex flex-wrap -m-2">
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="username" className="leading-7 text-sm text-gray-600">Username</label>
                                        <input type="text" id="username" name="username" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.username} onChange={handleChange} />
                                    </div>
                                </div>

                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="password" className="leading-7 text-sm text-gray-600">Password</label>
                                        <input type="password" id="password" name="password" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.password} onChange={handleChange} />
                                    </div>
                                </div>

                                <div className="flex justify-between w-full">
                                    <div className="p-2 w-full">
                                        <button type="submit" className="flex mx-auto text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </section>
        </div>
    );
}

export default Page;
