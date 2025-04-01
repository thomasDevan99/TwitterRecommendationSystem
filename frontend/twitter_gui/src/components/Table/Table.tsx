import React from 'react'

interface TableProps {
    data: any
}

export const Table = () => {
    return (
        <div className='mx-auto'>
            <table className='border-2 border-black'>
                <thead>
                    <tr className='border-2 border-black'>
                        <th className='px-4 border-2 border-black' scope='column'>Tweet</th>
                        <th className='px-4 border-2 border-black' scope='column'># Retweets</th>
                        <th className='px-4 border-2 border-black' scope='column'># Likes</th>
                    </tr>
                </thead>
                <tbody className='border-2 border-black'>
                    <tr className='border-2 border-black'>
                        <td className='px-4 border-2 border-black'>
                            Tigers win! Bruce Pearl sets conference record with 18 SEC victories this season!
                        </td>
                        <td className='px-4 border-2 border-black'>
                            4253
                        </td>
                        <td className='px-4 border-2 border-black'>
                            8982
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}