export const imageFileFilter = (req, file, callback) => {
    if (!file.originalname.match(/\.(jpg|jpeg|png|gif|pdf)$/)) {
        return callback(new Error('Only image files are allowed!'), false);
    }
    callback(null, true);
};