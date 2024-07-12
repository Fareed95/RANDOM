"use client"
import { useRouter } from "next/navigation";
import { useState } from 'react';

function FormPage() {
    const router = useRouter();
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        phone: "",
        address: ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://127.0.0.1:8000/formslist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            console.log('Form submitted successfully!');
            router.push('/Display'); // Redirect to Display page
        } else {
            console.log('Failed to submit the form');
        }
    };

    return (
        <div>
            <>
                <div className="flex items-center justify-center h-[7rem] ">
                    <div className="text-6xl font-bold bg-gradient-to-r from-blue-500 via-purple-400 to-pink-700 bg-clip-text text-transparent transition-colors duration-1000
                        hover:bg-gradient-to-r hover:from-blue-800 hover:via-purple-600 hover:to-pink-400  ease-in  
                        ">
                        Fill the following FORM !
                    </div>
                </div>

                <section className="text-gray-600 body-font relative">
                    <div className="container px-5 py-24 mx-auto">
                        <div className="flex flex-col text-center w-full mb-12">
                            <p className="lg:w-2/3 mx-auto leading-relaxed text-base">Fill out the form below to see the deets on other page.</p>
                        </div>
                        <div className="lg:w-1/2 md:w-2/3 mx-auto">
                            <form onSubmit={handleSubmit}>
                                <div className="flex flex-wrap -m-2">
                                    <div className="p-2 w-full">
                                        <div className="relative">
                                            <label htmlFor="name" className="leading-7 text-sm text-gray-600">Full Name</label>
                                            <input type="text" id="name" name="name" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.name} onChange={handleChange} />
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
                                            <label htmlFor="phone" className="leading-7 text-sm text-gray-600">Phone Number</label>
                                            <input type="tel" id="phone" name="phone" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" value={formData.phone} onChange={handleChange} />
                                        </div>
                                    </div>
                                    <div className="p-2 w-full">
                                        <div className="relative">
                                            <label htmlFor="address" className="leading-7 text-sm text-gray-600">Address</label>
                                            <textarea id="address" name="address" className="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out" value={formData.address} onChange={handleChange}></textarea>
                                        </div>
                                    </div>
                                    <div className="p-2 w-full">
                                        <button type="submit" className="flex mx-auto text-white bg-blue-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Submit</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </section>
            </>
        </div>
    );
}

export default FormPage;
