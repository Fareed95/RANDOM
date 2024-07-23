"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from 'react';

function FormPage() {
    const router = useRouter();
    const [confirmp, setConfirmp] = useState(""); // Fixed state naming
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        first_name: "",
        last_name: ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const Cpass = (e) => {
        setConfirmp(e.target.value); // Update confirm password state
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const { password } = formData;

        console.log("Form submitted");
        console.log("Form Data:", formData);
        console.log("Confirm Password:", confirmp);

        if (password !== confirmp) { // Use confirmp here
            alert("Passwords do not match!");
            return;
        }

        if (formData.username === "" || formData.password === "" || formData.email === "") {
            alert("Please fill the form first");
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/users', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const responseData = await response.json();
            console.log("Response Data:", responseData);

            if (response.ok) {
                console.log('Form submitted successfully!');
                console.log(formData);
                router.push('/Display'); // Redirect to Display page
            } else {
                console.log('Failed to submit the form', responseData);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const { password } = formData;

    return (
        <div>
            <div className="flex items-center justify-center h-[7rem] ">
                <div className="text-6xl font-bold bg-gradient-to-r from-blue-500 via-purple-400 to-pink-700 bg-clip-text text-transparent transition-colors duration-1000 hover:bg-gradient-to-r hover:from-blue-800 hover:via-purple-600 hover:to-pink-400 ease-in">
                    SIGNUP!
                </div>
            </div>

            <section className="text-gray-600 body-font relative">
                <div className="container px-5 py-24 mx-auto">
                    <div className="flex flex-col text-center w-full mb-12">
                        <p className="lg:w-2/3 mx-auto leading-relaxed text-base">Fill out the form below to see the details on another page.</p>
                    </div>
                    <div className="lg:w-1/2 md:w-2/3 mx-auto">
                        <form onSubmit={handleSubmit}>
                            <div className="flex flex-wrap -m-2">
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="username" className="leading-7 text-sm text-gray-600">User Name</label>
                                        <input type="text" id="username" name="username" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.username} onChange={handleChange} />
                                    </div>
                                </div>
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="first_name" className="leading-7 text-sm text-gray-600">First Name</label>
                                        <input type="text" id="first_name" name="first_name" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.first_name} onChange={handleChange} />
                                    </div>
                                </div>
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="last_name" className="leading-7 text-sm text-gray-600">Last Name</label>
                                        <input type="text" id="last_name" name="last_name" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.last_name} onChange={handleChange} />
                                    </div>
                                </div>
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="email" className="leading-7 text-sm text-gray-600">Email</label>
                                        <input type="email" id="email" name="email" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.email} onChange={handleChange} />
                                    </div>
                                </div>
                                
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="password" className="leading-7 text-sm text-gray-600">Password</label>
                                        <input type="password" id="password" name="password" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.password} onChange={handleChange} />
                                    </div>
                                </div>
                                <div className="p-2 w-full">
                                    <div className="relative">
                                        <label htmlFor="Cpassword" className="leading-7 text-sm text-gray-600">Confirm Password</label>
                                        <input type="password" id="Cpassword" name="Cpassword" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={confirmp} onChange={Cpass} />
                                        <div className={`${password !== confirmp ? 'text-red-700' : 'text-white'} mt-2`}>
                                            {password !== confirmp && "The passwords don't match"}
                                        </div>
                                    </div>
                                </div>
                                <div className="flex justify-between w-full">

                                <div className="p-2 w-full">
                                        <button type="submit" className="flex mx-auto text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Submit</button>
                                    </div>
                                    <div className="p-2 w-full flex text-center">
                                        <Link href={"/Login"}>
                                            <label className="flex">Already a user?
                                                <button className="flex mx-auto text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Login</button>
                                            </label>
                                        </Link>
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

export default FormPage;
