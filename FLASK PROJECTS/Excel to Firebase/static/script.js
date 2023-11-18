
const dragArea=document.querySelector('.drag-area');
const dragtext=document.querySelector('.header');

let button =document.querySelector('.button');
let input=document.querySelector('input');
let file;

button.onclick=()=>{
    input.click();
};

//wen browse
input.addEventListener('change',function(){
    file=this.files[0];
    dragArea.classList.add('active');
    displayFile();
});

//When file is inside the drag area
dragArea.addEventListener('dragover',(event)=>{
    event.preventDefault();
    dragtext.textContent="Release to upload"
    dragArea.classList.add('active');
    //console.log('File is inside the drag area');
});

//When file leaves the drag area
dragArea.addEventListener('dragleave',()=>{
    dragtext.textContent="Drag & Drop";
    dragArea.classList.remove('active');
    //console.log("File left the drag area");
});

//When the file is dropped in the drag area
dragArea.addEventListener('drop',(event)=>{
    event.preventDefault();

    file=event.dataTransfer.files[0];
    displayFile();
    //console.log("the file is droped in the drag area");
});


function displayFile(){
    let fileType=file.type;
    //console.log(file);
    if(fileType=='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'){
        let fileReader=new FileReader();
        fileReader.onload=()=>{
            let fileURL =fileReader.result;
            console.log(fileURL)
        };
        fileReader.readAsDataURL(file);
        console.log(fileType);
    }
    else if(fileType=='application/vnd.ms-excel'){
        let fileReader=new FileReader();
        fileReader.onload=()=>{
            let fileURL =fileReader.result;
            console.log(fileURL)
        };
        fileReader.readAsDataURL(file);
        console.log(fileType);
    }
    else{
        alert('This file type is not supported.');
        dragArea.classList.remove('active');
        dragtext.textContent="Drag & Drop";
    }
}




