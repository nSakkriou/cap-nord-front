export const getAllBlog = () => {
    return fetch("http://nathansakkriou.com/api/v1/cap-nord/blogs").then(res => res.json())
}