import java.io.File
import java.io.InputStream


object Constants{
    const val FILE_NAME = "input 4.txt"
}

fun main(args: Array<String>){
    val inputStr: inputStream = File(FILE_NAME).inputStream().bufferedReader().use{ it.readText() }
    // println(inputStr)
}

//Honestly, I give up on trying Kotlin. Let's use Python for this question instead