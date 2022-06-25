import React ,{useState} from 'react';
import AWS from 'aws-sdk'
import { uploadfile } from '../service';
import "./../App.css"



const S3_BUCKET ='asu-serverless-appbucket';
const REGION ='us-east-1';


AWS.config.update({
    accessKeyId: 'AKIA4LLQUASXXASLL676',
    secretAccessKey: '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'
})

const myBucket = new AWS.S3({
    params: { Bucket: S3_BUCKET},
    region: REGION,
})

const FileUploader = () => {

    const [progress , setProgress] = useState(0);
    const [selectedFile, setSelectedFile] = useState(null);
    const [inputData, setInputData] = useState("");

    const handleFileInput = (e) => {
        setSelectedFile(e.target.files[0]);
    }

    const handleInputData =(e) => {
        setInputData(e.target.value)
    }


    const uploadFile = (file) => {

        const params = {
            ACL: 'public-read',
            Body: file,
            Bucket: S3_BUCKET,
            Key: file.name
        };

        const apiParams = {
          inputText: inputData,
          filePath: S3_BUCKET+"/"+file.name
        };
        
        var temp = uploadfile(apiParams)
        console.log(temp)

        myBucket.upload(params)
            .on('httpUploadProgress', (evt) => {
                setProgress(Math.round((evt.loaded / evt.total) * 100))
            })
            .send((err) => {
                if (err) console.log(err)
            })
          
    }


    return <div>
        <div>
          Text Input: <input type="text" value={inputData} onChange={handleInputData}></input>
        </div>
        <div>
          File Input: <input type="file" onChange={handleFileInput}/>
        </div>
        <div>
          <button onClick={() => uploadFile(selectedFile)}> Upload to S3</button>
        </div>
        
    </div>
}

export default FileUploader;